import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { HeaderComponent } from './layout/header/header.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, HeaderComponent],
  template: `
    <app-header />
    <main class="main-content">
      <router-outlet />
    </main>
  `,
  styleUrl: './app.scss',
})
export class App {}
